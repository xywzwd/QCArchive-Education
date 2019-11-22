# AUTO GENERATED FILE - DO NOT EDIT

''appheader <- function(children=NULL, id=NULL, className=NULL, fixed=NULL, tag=NULL) {
    
    props <- list(children=children, id=id, className=className, fixed=fixed, tag=tag)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'appheader',
        namespace = 'qcedu',
        propNames = c('children', 'id', 'className', 'fixed', 'tag'),
        package = 'qcedu'
        )

    structure(component, class = c('dash_component', 'list'))
}
