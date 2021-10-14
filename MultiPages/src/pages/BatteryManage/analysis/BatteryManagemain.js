import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/globalVar.js'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import 'normalize.css/normalize.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

import * as echarts from 'echarts';

Vue.use(VueAxios, axios)
Vue.use(ElementUI);
Vue.use(echarts)
Vue.use(ViewUI);
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#batterymanageapp')
