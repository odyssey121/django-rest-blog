<template>
  <div id="main-layout">
    <TheHeader @sidenavToggle="toggleView" />
    <TheSideNav @close="toggleView" :show="showToggle"></TheSideNav>
    <div class="container">
      <nuxt />
    </div>
  </div>
</template>

<script>
import TheHeader from "~/components/Navigation/TheHeader";
import TheSideNav from "~/components/Navigation/TheSideNav";
import { mapGetters, mapActions } from "vuex";

export default {
  components: { TheHeader, TheSideNav },

  created() {
    this.$q.loadingBar.setDefaults({
      color: "orange",
      size: "2px",
      position: "top"
    });
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

<style scoped>

</style>
