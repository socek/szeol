var routes = {
    order_form: () => {
        return import('./order_form.js');
    }
}
function simple_route(name) {
    routes[name]().then(function(module) {
        module.init();
    }).catch(function(err) {
        console.log('Failed to load "'+ name +'"', err);
    });
}

window.simple_route = simple_route;
