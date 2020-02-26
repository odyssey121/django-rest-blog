<template>
  <div
    class="drawer-toggle"
    role="button"
    @click="$emit('toggle')">
    <div class="bar"></div>
    <div class="bar"></div>
    <div class="bar"></div>
  </div>
</template>

<style scoped>
.drawer-toggle {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 40%;
  width: 28px;
  cursor: pointer;
  margin-right: 1.3rem;
}

@media (min-width: 768px) {
  .drawer-toggle {
    display: none;
  }
}

.drawer-toggle .bar {
  width: 90%;
  height: 2px;
  background-color: var(--text-grey);
}
</style>
