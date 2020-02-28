<template>
  <div v-if="posts">
    <div class="post-layout" v-for="post in posts" :key="post.id">
      <post-item :post='post'/>
    </div>
  </div>
</template>

<script>
import PostItem from "@/components/PostItem";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { PostItem },
  computed: {
    posts() {
      return this.$store.getters.getPosts;
    }
  }
};
</script>

<style lang="scss" scoped>
.post-layout {
  width: 80%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  display: flex;
}
</style>
