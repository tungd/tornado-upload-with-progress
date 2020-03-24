const { fusebox } = require('fuse-box')

const fuse = fusebox({
  entry: 'main.tsx',
  target: 'browser',

  devServer: {
    hmrServer: {
      connectionURL: 'ws://localhost:4444'
    }
  },

  webIndex: {
    publicPath: '/static',
  }
})

fuse.runDev()
