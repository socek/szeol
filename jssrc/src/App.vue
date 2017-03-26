<template>
  <div id="app">
    <div class="right_col" role="main">
      <!-- top tiles -->
      <div class="row tile_count">
        <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
          <span class="count_top"><i class="fa fa-user"></i>Total Clients</span>
          <div class="count">0</div>
          <span class="count_bottom"><i class="green">0 </i> {% trans "From last Week" %}</span>
        </div>
        <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
          <span class="count_top"><i class="fa fa-user"></i> {% trans "Total Products" %}</span>
          <div class="count">{{ statistics.products }}</div>
          <span class="count_bottom"><i class="green">{{ statistics.products_created }} </i> {% trans "From last Week" %}</span>
        </div>
        <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
          <span class="count_top"><i class="fa fa-user"></i> {% trans "Orders" %}</span>
          <div class="count">0</div>
          <span class="count_bottom"><i class="green">0 </i> {% trans "From last Week" %}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      statistics: {
        products: 0,
        products_created: 1
      }
    }
  }
}
</script>
