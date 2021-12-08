<template>
  <div class="trends">
    <h1>Trend</h1>
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
import { defineComponent, reactive, computed } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import VueHighcharts from "vue3-highcharts";

export default defineComponent({
  name: "Trends",

  components: {
    VueHighcharts,
  },

  setup() {
    const route = useRoute();

    const state = reactive({
      trend: {
        id: null,
        keyword: null,
        value: [],
      },
    });

    const chartOptions = computed(() => {
      return {
        title: {
          text: state.trend.keyword,
        },
        xAxis: {
          categories: ["Apples", "Bananas", "Oranges"],
        },
        series: [
          {
            name: "検索ボリューム",
            data: state.trend.value,
          },
        ],
      };
    });

    const getTrends = () => {
      axios.get("/trends/" + route.params.id).then((res) => {
        if (res && res.data) {
          state.trend = res.data;
        }
      });
    };

    getTrends();

    return {
      state,
      chartOptions,
    };
  },
});
</script>

<style>
.vue-highcharts {
  width: 100%;
}
</style>