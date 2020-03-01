<template>
  <div v-if="posts">
    <div v-for="post in posts" :key="post.id">
      <post-item :post="post" />
    </div>
  </div>
</template>

<script>
import PostItem from "@/components/PostItem";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { PostItem },
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
</style>
