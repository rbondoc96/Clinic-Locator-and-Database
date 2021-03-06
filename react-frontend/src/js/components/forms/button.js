import React from "react"

export default function Button({
    type="button",
    id,
    href,
    children,
    secondary,
    onClick,
    openNewTab=false,
    size="small"
}) {

    return(
        <>
        {href
        ? <a href={href} target={openNewTab ? "_blank" : ""}>
            <button id={id} type="button" className={`button ${secondary? "button-secondary":""} ${size=="small"? "button--small":""}`} onClick={onClick}>
                {children}
            </button>
        </a>
        : <button id={id} type={type} className={`button ${secondary? "button-secondary":""} ${size=="small"? "button--small":""}`} onClick={onClick}>
            {children}
        </button>
        }
        </>
    )
}