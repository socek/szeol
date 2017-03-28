import Vue from 'vue'
Vue.component('order-form', {
  delimiters: ['${', '}'],
  props: ['form'],
  template: '#order_form_template'
});

Vue.component('form-text-input', {
  delimiters: ['${', '}'],
  props: ['field'],
  template: '#form_text_input'
});

export function init() {
  new Vue({
    delimiters: ['${', '}'],
    el: '#order_create_app',
    data: {
      form: {
        name: 'myformname',
        first: {
          id_for_label: 'idforlabelhej',
          help_text: 'myhelptext',
          required: false,
          name: 'myfirst',
          value: 'myval',
        }
      }
    }
  });
};
