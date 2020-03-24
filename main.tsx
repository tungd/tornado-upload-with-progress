import * as React from 'react'
import * as ReactDOM from 'react-dom'

import 'antd/dist/antd.css'
import { Upload as BaseUpload } from 'antd'


class Upload extends React.Component {

  onProgressChanged = e => console.log(e)

  render() {
    return (
      <BaseUpload action="/upload" listType="picture-card" onChange={this.onProgressChanged}>
        Upload
      </BaseUpload>
    )
  }
}


const main = () => ReactDOM.render(
  <Upload />,
  document.querySelector('body')
)

main()
