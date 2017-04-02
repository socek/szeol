import Vue from 'vue';

export default class SelfForm {
  constructor(el, component) {
    this.el = el;
    this.component = component;
  }

  run() {
    this.initComponent();
    fetch(window.location, this.formOptions).then(
      this.parseJson.bind(this)).then(
      this.renderTemplate.bind(this)).catch(
      this.parseJsonError.bind(this))
  }

  initComponent() {
    Vue.component('form-component', {
      delimiters: ['${', '}'],
      props: ['form'],
      template: this.component,
      methods: {
        submitData: function(event) {
          console.log(this.form.fields.description.value);
          console.log(this.form.fields.discount.value);
          console.log(this.form.fields.order_status.value);
          console.log(this.form.fields.payment_status.value);
        },
        change_radio_state: function(field, value, event) {
          console.log('a', field, value, event);
          console.log(field);
        }
      }
    });
  }

  get formOptions() {
    return {
      method: 'OPTIONS',
      credentials: 'same-origin'
    }
  }

  parseJson(response) {
    return response.json();
  }

  parseJsonError(ex) {
    console.log('parsing failed', ex);
  }

  renderTemplate(data) {
    console.log(data);
    new Vue({
      delimiters: ['${', '}'],
      el: this.el,
      data: data
    });
  }

  onSubmit(message, event) {
    console.log(this);
    console.log('b', message);
    console.log('c', event);
  }
};

