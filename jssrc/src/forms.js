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
        submitData: this.onSubmit.bind(this)
      }
    });
  }

  get formOptions() {
    return {
      method: 'OPTIONS',
      credentials: 'same-origin'
    }
  }

  get formElement() {
    return document.querySelector(this.el +' form');
  }

  formPost(formData) {
    return {
      method: 'POST',
      credentials: 'same-origin',
      body: formData
    }
  }

  parseJson(response) {
    return response.json();
  }

  parseJsonError(ex) {
    console.log('parsing failed', ex);
  }

  renderTemplate(data) {
    console.log(data.form.fields.order_status);
    if(this.vue) {
      this.vue.form.fields = data.form.fields;
    } else {
      this.vue = new Vue({
        delimiters: ['${', '}'],
        el: this.el,
        data: data,
        mounted: this.onCreation.bind(this)
      });
    };
  }

  onSubmit(event) {
    let formData = new FormData(this.formElement);
    console.log('here', this.vue.form.fields.order_status.value);

    fetch(window.location, this.formPost(formData)).then(
      this.parseJson.bind(this)).then(
      this.renderTemplate.bind(this)).catch(
      this.parseJsonError.bind(this))
  }

  onCreation() {
    let inputs = this.formElement.querySelectorAll(
      'label.active input[type=radio]');
    for(let input of inputs) {
      input.click();
    }
  }
};

