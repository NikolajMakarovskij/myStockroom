import globals from 'globals'
import pluginJs from '@eslint/js'
import pluginReactConfig from 'eslint-plugin-react/configs/recommended.js'
import { fixupConfigRules } from '@eslint/compat'

export default [
  {
    settings: { react: { version: 'detect' } },
    files: ['src/**/*jsx'],
    languageOptions: {
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
      },
      globals: {
        ...globals.browser,
      },
    },
    rules: {},
  },
  pluginJs.configs.recommended,
  ...fixupConfigRules(pluginReactConfig),
]
