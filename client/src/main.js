import 'bootstrap/dist/css/bootstrap.min.css'; // import bootstrap library
import BootstrapVue from 'bootstrap-vue'; // enable Bootstrap Vue library
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.use(BootstrapVue); // enable Bootstrap Vue library

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
