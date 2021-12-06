<template>
  <div class="trends">
    <h1>Trends</h1>
    <div v-for="trend in state.trends" :key="trend.id">
      <div class="title margin-r1">title: {{ trend.id }}</div>
      <div class="status margin-r1">status: {{ trend.keyword }}</div>
    </div>
  </div>
</template>

<script>
import { defineComponent, reactive } from "vue";
import axios from "axios";

const baseURL = "http://localhost:8000/trends";

export default defineComponent({
  name: "Trends",
  setup() {
    const state = reactive({
      trends: [],
    });

    // add start
    const getTrends = () => {
      axios.get(baseURL).then((res) => {
        if (res && res.data) {
          state.trends = res.data.resBody;
        }
      });
    };

    getTrends();
    // end

    return {
      state,
      getTrends,
    };
  },
});
</script>