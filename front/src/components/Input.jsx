import React from "react";

export default function Input({labelName, typed}) {
    return (
        <React.Fragment>
            <label htmlFor="">{labelName}</label>
            <input type={typed} name="" id="" />
        </React.Fragment>
    )
}