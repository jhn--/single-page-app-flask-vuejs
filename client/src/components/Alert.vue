// Challenges:

// Think about where showMessage should be set to false. Update your code.
// Try using the Alert component to display errors.
// Refactor the alert to be dismissible.

<template>
  <!-- <p>It works</p> -->
  <div>
      <b-alert variant="success" show>{{ message }}</b-alert>
      <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
