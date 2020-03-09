type RedBlackNode<T> = {
    isRed: boolean
    left: RedBlackNode<T>,
    center: RedBlackNode<T>,
    right: RedBlackNode<T>,
    value: T
}

function Draw(node: RedBlackNode<unknown>) {
    // go through the depth
    // calculate left position as center of row below
    // calculate top as depth
    // if is leaf position flush
}