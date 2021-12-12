<template>
  <div class="p-2 bg-white filter rounded drop-shadow">
    <div
      :class="{
        'h-4 w-4/12 mx-auto my-2 animate-pulse bg-gray-100 rounded-full':
          !title,
      }"
    >
      {{ title }}
    </div>
    <vue-highcharts
      type="chart"
      :options="chartOptions"
      :redrawOnUpdate="true"
      :oneToOneUpdate="false"
      :animateOnUpdate="true"
      @rendered="onRender"
      @update="onUpdate"
      @destroy="onDestroy"
    />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import VueHighcharts from "vue3-highcharts";

export default defineComponent({
  components: {
    VueHighcharts,
  },
  props: {
    title: {
      type: String,
      required: false,
      default: "",
    },
    chartOptions,
  },
});
</script>

<style scoped>
.vue-highcharts {
  width: 100%;
}
</style>