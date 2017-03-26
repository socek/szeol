import Vue from 'vue'

Vue.component('my-component', {
  delimiters: ['${', '}'],
  template: '#mytemp',
  props: ["statistics"]
})


$.ajax({
    url: "/stats",
    context: document.body
}).done((data) => {
  new Vue({
      delimiters: ['${', '}'],
      el: '#app',
      data: data

    })
});


