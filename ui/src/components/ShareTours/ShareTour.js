import React, { useState, useEffect, useRef } from 'react'
import { Button, Header } from 'semantic-ui-react'
import { CopyToClipboard } from 'react-copy-to-clipboard'

import './ShareTour.less'

export default function ShareTour() {
  const uri = window.location.href
  const [copied, setCopied] = useState(false)
  const [url, setUrl] = useState(uri)
  const timeout = useRef()

  function onCopyUrl() {
    if (!copied) {
      setUrl(uri)
      setCopied(true)
      timeout.current = setTimeout(() => setCopied(false), 1000)
    }
  }

  useEffect(() => {
    if (timeout.current) {
      clearTimeout(timeout.current)
    }
  }, [])

  return (
    <div>
      <CopyToClipboard text={url} onCopy={onCopyUrl}>
        <Button size='big' icon='share alternate' className='btnshare' />
      </CopyToClipboard>
      {copied ? (
        <Header as='h5' ref={timeout} className='copied' color='pink'>
          copied!
        </Header>
      ) : null}
    </div>
  )
}
