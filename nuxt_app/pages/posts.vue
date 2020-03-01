<template>
  <div class="row q-col">
    <div class="col-9">
      <post-list v-if="articles" :posts="articles" />
    </div>
    <div class="col-3">
      <side-bar :categories="categories"></side-bar>
    </div>
  </div>
</template>

<script>
import PostList from "@/components/PostList";
import SideBar from "@/components/SideBar";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { PostList, SideBar },

  async asyncData({ $axios, error }) {
    const response = await $axios.get("api");
    try {
      let result = {};
      const data = (
        await Promise.all(
          Object.keys(response.data).map(item => $axios.get(`/api/${item}`))
        )
      ).forEach(
        resp => (result[resp.config.url.split("/api/")[1]] = resp.data)
      );
      return result;
    } catch (err) {
      console.log(err);
      error({ statusCode: 500, message: "fdsfs" });
    }
  }
};
</script>

<style scoped>
</style>
