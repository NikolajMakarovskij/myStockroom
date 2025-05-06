import { React } from 'react'
import IndexSignature from '../appSignature/IndexSignature'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const signatureRouter = [
  { path: '/signature', element: [<NavBar key='signature' drawerWidth={customWidth} content={<IndexSignature />} />] },
]

export default signatureRouter
