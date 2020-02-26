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
export default {
  components: { TheHeader, TheSideNav },
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

<style>

</style>
