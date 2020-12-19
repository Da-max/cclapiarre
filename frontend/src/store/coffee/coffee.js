import apolloClient from '@/vue-apollo'

import COFFEE_ALL from '@/graphql/Coffee/CoffeeAll.gql'

export default {
  namespaced: true,
  state: () => ({
    coffees: [],
    coffeeOrderedId: 0,
    order: []
  }),

  mutations: {
    SET_COFFEE (state, coffees) {
      state.coffees = coffees
    },
    ADD_COFFEE_ORDER (state, coffee) {
      state.order.push({
        id: state.coffeeOrderedId,
        coffee,
        weight: null,
        type: null,
        amount: 0
      })
      state.coffeeOrderedId++
    },
    REMOVE_COFFEE_ORDER (state, orderId) {
      state.order = state.order.filter((coffee) => coffee.id !== orderId)
    },

    SET_COFFEE_ORDER_WEIGHT (state, { orderId, weight }) {
      state.order.find((coffee) => coffee.id === orderId).weight = weight
    }
  },
  actions: {
    async getCoffees ({ commit }) {
      commit('START_LOADING', null, { root: true })
      try {
        const response = await apolloClient.query({ query: COFFEE_ALL })
        commit('SET_COFFEE', response.data.coffee.edges)
      } catch (e) {
        commit('alert/ADD_ALERT', {
          header: false,
          body: `Une erreur est survenue, merci de réessayer : ${e}`,
          status: 'error',
          close: true
        }, { root: true })
      } finally {
        commit('END_LOADING', null, { root: true })
      }
    }
  }
}
