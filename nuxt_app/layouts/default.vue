<template>
  <div id="main-layout">
    <TheHeader @sidenavToggle="toggleView" />
    <TheSideNav @close="toggleView" :show="showToggle"></TheSideNav>
    <nuxt />
  </div>
</template>

<script>
import TheHeader from "~/components/Navigation/TheHeader";
import TheSideNav from "~/components/Navigation/TheSideNav";
import { mapGetters, mapActions } from "vuex";
export default {
  components: { TheHeader, TheSideNav },
  created() {
    this.$store.dispatch("getPosts");
  },
  data() {
    return {
      showToggle: false
    };
  },
  methods: {
    toggleView() {
      this.showToggle = !this.showToggle;
    }
  }
};
</script>

<style></style>
