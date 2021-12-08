<template>
  <div class="trends">
    <h1>Trends</h1>
    <div v-for="trend in state.trends" :key="trend.id">
      <div class="status margin-r1">
        <router-link :to="{ name: 'trend', params: { id: trend.id } }">
          keyword: {{ trend.keyword }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, reactive } from "vue";
import axios from "axios";

export default defineComponent({
  name: "Trends",
  setup() {
    const state = reactive({
      trends: [],
    });

    const getTrends = () => {
      axios.get("/trends").then((res) => {
        if (res && res.data) {
          state.trends = res.data;
        }
      });
    };

    getTrends();

    return {
      state,
    };
  },
});
</script>