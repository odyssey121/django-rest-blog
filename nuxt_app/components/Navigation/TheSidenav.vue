<template>
  <div class="sidenav-container">
    <div v-if="show" class="sidenav-backdrop" @click="$emit('close')"></div>
    <transition name="slide-side">
      <div v-if="show" class="sidenav">
        <q-list bordered class="nav-list" @click="$emit('close')">
          <q-item>
            <q-item-section>
              <nuxt-link to="/">WD BLOG</nuxt-link>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <nuxt-link to="/posts">Blog</nuxt-link>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <nuxt-link to="/about">About</nuxt-link>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>Avatar-type icon</q-item-section>
          </q-item>
          <!-- <li class="nav-item"><nuxt-link to="/posts">Blog</nuxt-link></li>
        <li class="nav-item"><nuxt-link to="/about">About</nuxt-link></li>
          <li class="nav-item"><nuxt-link to="/admin">Admin</nuxt-link></li>-->
        </q-list>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "TheSidenav",
  components: {},
  props: {
    show: {
      type: Boolean,
      default: false
    }
  }
};
</script>


<style scoped>
.sidenav-container {
  height: 100%;
  width: 100%;
}

.sidenav-backdrop {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1000;
  position: fixed;
  top: 0;
  left: 0;
}

.sidenav {
  height: 100%;
  width: 300px;
  background-color: white;
  z-index: 10000;
  position: fixed;
  top: 0;
  left: 0;
  box-sizing: border-box;
}

.slide-side-enter-active,
.slide-side-leave-active {
  transition: all 0.3s ease-out;
}
.slide-side-enter,
.slide-side-leave-to {
  transform: translateX(-100%);
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin: 20px 0;
}

.nav-item a {
  text-decoration: none;
  color: black;
  font-size: 1.5rem;
  font-family: var(--Abel);
}

.nav-item a:hover,
.nav-item a:active {
  color: var(--midnight);
}
</style>
