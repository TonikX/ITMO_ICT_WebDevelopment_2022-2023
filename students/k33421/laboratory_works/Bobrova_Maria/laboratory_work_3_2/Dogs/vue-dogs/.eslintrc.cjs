/* eslint-env node */
module.exports = {
  globals: {
    "$": true,
    "jQuery": true
  },
  root: true,
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended'
  ],
  parserOptions: {
    ecmaVersion: 'latest'
  }
}
