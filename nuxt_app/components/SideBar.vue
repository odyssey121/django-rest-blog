<template>
  <div class="side-bar">
    <div class="text-center text-h5">Categories</div>
    <ul>
      <li v-for="category in categories" :key="category.id">
        <q-chip color="primary" text-color="white">
          <a href="#">{{ category.name }}</a>
        </q-chip>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  props: {
    categories: {
      type: Array,
      default: []
    }
  }
};
</script>

<style scoped>
.side-bar {
  padding: 1rem;
  margin-left: 1rem;
}
.side-bar > div {
  border-bottom: 1px solid #ccc;
}
</style>