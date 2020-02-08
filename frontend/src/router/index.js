import Vue from 'vue'
import VueRouter from 'vue-router'
import CoffeeCommand from '../views/CoffeeCommand'

Vue.use(VueRouter)

const routes = [
  {
    path: '/cafe/commander-du-cafe',
    name: 'coffee_command',
    component: CoffeeCommand
  },
  {
    path: '/commande/commander-des-agrumes',
    name: 'citrus_command',
    component: function () {
      return import('../views/CitrusCommand.vue')
    }
  },
  {
    path: '/pate/commander-des-pates',
    name: 'pasta_command',
    component: function () {
      return import ('../views/PastaCommand.vue')
    }
  }
  /*{
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" *//* '../views/About.vue')
    }
  },
  {
    path: '/a',
    name: 'pageA',
    component: function () {
      return import('../views/PageA.vue')
    },
    children: [
      {
        path: 'c',
        name: 'a.c',
        component: PageC
      },
      {
        path: 'b',
        name: 'a.b',
        component: PageB
      }
    ]
  }, 
  {
    path: '*',
    redirect: '/'
  }*/
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
