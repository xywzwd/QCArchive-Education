% Auto-generated: do not edit by hand
\name{''appsidebarnav}

\alias{''appsidebarnav}

\title{appsidebarnav component}

\description{
CoreUI sidebar nav component.  This component manages the location in a multi-page much as Dash Core Components `Location` component. It is also compatible with the Dash Core Components `Link` component. See https://dash.plot.ly/urls for details.
}

\usage{
''appsidebarnav(children=NULL, id=NULL, className=NULL, pathname=NULL, search=NULL, hash=NULL,
href=NULL, refresh=NULL, navConfig=NULL, navFunc=NULL, isOpen=NULL,
staticContext=NULL, tag=NULL, style=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children, defaults to `navConfig.items`.}

\item{id}{Character. The ID used to identify this component in Dash callbacks, defaults to `appsidebarnav`.}

\item{className}{Character. The CSS class name, defaults to `sidebar-nav`.}

\item{pathname}{Character. The pathname in window.location - e.g., "/my/full/pathname"}

\item{search}{Character. The search in window.location - e.g., "?myargument=1"}

\item{hash}{Character. The hash in window.location - e.g., "#myhash"}

\item{href}{Character. The href in window.location - e.g., "/my/full/pathname?myargument=1#myhash"}

\item{refresh}{Logical. Refresh the page when the location is updated? Default to `true`.}

\item{navConfig}{Logical | numeric | character | named list | unnamed list. }

\item{navFunc}{Character. TODO document this.}

\item{isOpen}{Logical. The isOpen flag, defaults to `false`.}

\item{staticContext}{Logical | numeric | character | named list | unnamed list. TODO document this.}

\item{tag}{Character. The HTML tag, defaults to `nav`.}

\item{style}{Logical | numeric | character | named list | unnamed list. }
}
