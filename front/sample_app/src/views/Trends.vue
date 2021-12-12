<template>
  <div class="trends">
    <h1>Trends</h1>
    <div
      v-for="trend in trends"
      :key="trend.id"
      class="w-3/6 h-12 mx-auto my-2 bg-white filter rounded drop-shadow"
    >
      <router-link :to="{ name: 'trend', params: { id: trend.id } }">
        <div class="w-full h-full inline-block align-middle">
          keyword: {{ trend.keyword }}
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";
import axios from "axios";

export default defineComponent({
  name: "Trends",
  setup() {
    const store = useStore();

    const getTrends = () => {
      axios.get("/trends").then((res) => {
        if (res && res.data) {
          store.commit("setTrends", res.data);
        }
      });
    };

    getTrends();

    return {
      trends: computed(() => store.state.trends),
    };
  },
});
</script>