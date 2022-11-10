import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeIndexPredict from '@/page/predicttionPage/HomeIndex.vue'
import HomeIndexAdd from '@/page/add_data/HomeIndex.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeIndexPredict
  },
  {
    path: '/AddData',
    name: 'Add',
    component: HomeIndexAdd,
  }
]

const router = new VueRouter({
  routes
})

export default router
