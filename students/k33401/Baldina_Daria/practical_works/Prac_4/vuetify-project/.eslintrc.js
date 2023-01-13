module.exports = {
  root: true,
  env: {
    node: true,
  },
  parser: 'vue-eslint-parser', // Adding this line works perfectly
  extends: [
        'plugin:vue/base',
        'eslint:recommended',
        'plugin:vue/vue3-recommended', 
        'plugin:vue/essential',
        'plugin:@typescript-eslint/recommended',     // caused by this line
        'plugin:prettier/recommended',
        'eslint-config-prettier'
    ],
}
