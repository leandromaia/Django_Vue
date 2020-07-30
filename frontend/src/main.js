import Vue from 'vue'
import App1 from './App1.vue'
import App2 from './App2.vue'
import TestForm from "./TestForm";

Vue.config.productionTip = false

new Vue({
  render: h => h(App1),
}).$mount('#app1')

new Vue({
  render: h => h(App2),
}).$mount('#app2')

new Vue({
  render: h => h(TestForm),
}).$mount('#test-form')