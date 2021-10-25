import Vue from 'vue'
import TestForm from "./TestForm";

import axios from 'axios'

Vue.use(axios)

Vue.config.productionTip = false

new Vue({
  render: h => h(TestForm),
}).$mount('#test-form')