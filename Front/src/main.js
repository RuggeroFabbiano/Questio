import Vue from "vue";
import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;

Vue.filter('capitalize', function(value) {
  if (!value) return '';
  value = value.toString();
  return value.charAt(0).toUpperCase() + value.slice(1);
})
Vue.filter('questionize', function(value) {
  if (!value) return '';
  value = value.toString();
  if (value.charAt(value.length - 1) != "?") {return value + "?";}
  return value;
})

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
