import Vue from 'vue'
import VueRouter from 'vue-router'

import store from '../store/index'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/compte/liste-des-adherents',
    name: 'MembersList',
    component: () => import('../views/Registration/MembersList.vue'),
    beforeEnter: (to, from, next) => {
      const currentUser = store.state.auth.currentUser
      if (currentUser && currentUser.username) {
        next()
      } else {
        next(`/compte/connexion?next=${to.path}`)
      }
    }
  },
  {
    path: '/compte/connexion',
    name: 'Login',
    component: () => import('../views/Registration/Login.vue')
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
