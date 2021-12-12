<template>
  <div class="trends">
    <h1>Trend</h1>
    <div class="grid grid-cols-2 gap-4">
      <ChartCard :title="state.trend.keyword" :chartOprion="lineChartOptions" />
      <ChartCard :title="state.trend.keyword" :chartOprion="pieChartOptions" />
    </div>
  </div>
</template>

<script>
import { defineComponent, reactive, computed } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import ChartCard from "@/components/ChartCard.vue";

export default defineComponent({
  name: "Trend",

  components: {
    ChartCard,
  },

  setup() {
    const route = useRoute();

    const state = reactive({
      trend: {
        id: null,
        keyword: null,
        data: [],
      },
    });

    const getTrend = () => {
      axios.get("/trends/" + route.params.id).then((res) => {
        if (res && res.data) {
          state.trend = res.data;
        }
      });
    };

    getTrend();

    const lineChartOptions = computed(() => {
      return {
        title: {
          text: "",
        },
        xAxis: {
          tickInterval: 20, //目盛り間隔
          categories: state.trend.data.xAxis,
        },
        series: [
          {
            name: "検索ボリューム",
            data: state.trend.data.series,
          },
        ],
      };
    });

    const pieChartOptions = computed(() => {
      return {
        chart: {
          type: "pie",
        },
        title: {
          text: "",
        },
        series: [
          {
            name: "Brands",
            colorByPoint: true,
            data: [
              {
                name: "Chrome",
                y: 61.41,
              },
              {
                name: "Internet Explorer",
                y: 11.84,
              },
              {
                name: "Firefox",
                y: 10.85,
              },
              {
                name: "Edge",
                y: 4.67,
              },
              {
                name: "Safari",
                y: 4.18,
              },
              {
                name: "Sogou Explorer",
                y: 1.64,
              },
              {
                name: "Opera",
                y: 1.6,
              },
              {
                name: "QQ",
                y: 1.2,
              },
              {
                name: "Other",
                y: 2.61,
              },
            ],
          },
        ],
      };
    });

    return {
      state,
      lineChartOptions,
      pieChartOptions,
    };
  },
});
</script>