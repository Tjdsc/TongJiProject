import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DataUpload from "../views/DataUploadView.vue"
import DataProcess from "../views/DataProcessView"
import DataMonitor from "../views/DataMonitorView"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    keepAlive: true,
  },
  {
    path: '/DataUploadView',
    name: 'DataUpload',
    component: DataUpload,
    keepAlive: true,
  },
  {
    path:'/DataProcessView',
    name: 'DataProcess',
    component: DataProcess,
    keepAlive: true,
  },
  {
    path:'/DataMonitorView',
    name: 'DataMonitor',
    component: DataMonitor,
    keepAlive: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
