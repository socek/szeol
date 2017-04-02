import Vue from 'vue';
import SelfForm from './forms.js';

export function init() {
  let form = new SelfForm('#order_create_app', '#order_form_template');
  form.run();
};
