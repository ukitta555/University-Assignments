import React, { useState } from "react"

const useField = (type: string) => {
  const [value, setValue] = useState<string>('')
  const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (type === 'number') {
      console.log(Number(event.target.value), event.target.value)
      if (!isNaN(Number(event.target.value)) && Number(event.target.value) >= 0) {
        setValue(event.target.value as string)
      }
    }
    else {
      setValue(event.target.value as string)
    }
  }

  return {
    type,
    value,
    onChange
  }
}

export default useField