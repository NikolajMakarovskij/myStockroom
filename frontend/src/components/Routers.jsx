import { React } from 'react'
import { createBrowserRouter } from 'react-router-dom'
import NavBar from './appHome/NavBar'
import Home from './appHome/Home'
import workplaceRouter from './appWorkplace/workplaceRouter'
import employeeRouter from './appEmployee/employeeRouter'
import counterpertyRouter from './appCounterparty/counterpertyRouter'
import consumablesRouter from './appConsumables/consumablesRouter'
import accessoriesRouter from './appConsumables/accessoriesRouter'
import accountingRouter from './appAccounting/accountingRouter'
import deviceRouter from './appDevice/deviceRouter'
import stockConsumablesRouter from './appStock/stockConsumablesRouter'
import stockAccessoriesRouter from './appStock/stockAccessoriesRouter'
import stockDeviceRouter from './appStock/stockDeviceRouter'
import decommissionRouter from './appDecommission/decommissionRouter'
import disposalRouter from './appDisposal/disposalRouter'
import signatureRouter from './appSignature/signatureRouter'
import softwareRouter from './appSoftware/sofwareRouter'

const customWidth = 200
const Routers = createBrowserRouter([
  {
    path: '/',
    element: <NavBar key='home' drawerWidth={customWidth} content={<Home />} />,
  },
  ...workplaceRouter,
  ...employeeRouter,
  ...counterpertyRouter,
  ...consumablesRouter,
  ...accessoriesRouter,
  ...accountingRouter,
  ...deviceRouter,
  ...stockConsumablesRouter,
  ...stockAccessoriesRouter,
  ...stockDeviceRouter,
  ...decommissionRouter,
  ...disposalRouter,
  ...signatureRouter,
  ...softwareRouter,
])

export default Routers
