<template>
  <div class="header-container bg-grey-2">
    <header class="the-header">
      <TheSideNavToggle @toggle="$emit('sidenavToggle')" />
      <div class="logo">
        <nuxt-link to="/">SH BLOG</nuxt-link>
      </div>
      <div class="navigation-items">
        <q-tabs active-color="orange" style="height:100%;">
          <q-route-tab to="/posts" label="Blog" exact />
          <q-route-tab to="/about" label="About" exact />
        </q-tabs>
        <q-tabs active-color="orange" style="height:100%;">
          <q-route-tab to="/login" label="Login" exact />
        </q-tabs>
        <!-- <ul class="nav-list">
          <li class="nav-item">
            <nuxt-link to="/posts">Blog</nuxt-link>
          </li>

          <li class="nav-item">
            <nuxt-link to="/about">About</nuxt-link>
          </li>

          <li class="nav-item">
            <nuxt-link to="/admin">Admin</nuxt-link>
          </li>
        </ul>-->
      </div>
    </header>
  </div>
</template>

<script>
import TheSideNavToggle from "~/components/Navigation/TheSideNavToggle";
export default {
  name: "TheHeader",
  components: { TheSideNavToggle }
};
</script>
<style scoped>
.header-container {
  height: 54px;
  box-shadow: 0 1px 4px 0 rgba(0, 21, 41, 0.12);
  display: flex;
  justify-content: center;
  background: var(--sky);
}

.the-header {
  position: fixed;
  height: 54px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  z-index: 100;
  box-sizing: border-box;
  color: var(--text-grey);
}

.logo {
  width: 8rem;
  font-size: 1.3rem;
  margin-right: 1rem;
}

.logo a {
  text-decoration: none;
}

.navigation-items {
  display: none;
  height: 100%;
  width: 100%;
}

@media (min-width: 768px) {
  .navigation-items {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
}
@media (max-width: 768px) {
  .the-header {
    left: 0;
  }
}

.nav-list {
  margin: auto 0;
  height: 85%;
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  font-size: 1rem;
  margin: 0 1.3rem;
  align-self: center;
}

.nav-item a {
  text-decoration: none;
}

.nav-item a:hover,
.nav-item a:active,
.nav-item a.nuxt-link-active {
  color: var(--active-color);
}
</style>
