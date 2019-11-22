# AUTO GENERATED FILE - DO NOT EDIT

''datalist <- function(id=NULL, style=NULL) {
    
    props <- list(id=id, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'datalist',
        namespace = 'qcedu',
        propNames = c('id', 'style'),
        package = 'qcedu'
        )

    structure(component, class = c('dash_component', 'list'))
}
