import Vue from 'vue';
// import VueAxios from 'vue-axios';
import VueRouter from 'vue-router';

import axios from 'axios';
// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';

// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
// console.log(axios.defaults.headers);
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// var instance = axios.create({
//   baseURL: 'http://127.0.0.1:8000/api/',
//   timeout: 1000,
//   headers: {
//     'Z-nico': 'si',
//     'Access-Control-Allow-Origin': '*',
//     'Access-Control-Allow-Methods': 'GET, POST',
//     'Access-Control-Allow-Headers': 'Authorization, Lang'          
//   }
// });



Vue.use(VueRouter, axios)

// Components
import appSidebar from './sidebar/index.vue';
import appNav from './nav/index.vue';
import appPlaces from './places/index.vue';

const routes = [
  {path: '/places', component: appPlaces}
]

const router = new VueRouter({
  routes
})

new Vue({
  
  router: router,
  components: {
    appNav,
    appSidebar
  },
  created: function() {},
  mounted: function() {},
  destroyed: function() {}

}).$mount('#app')

