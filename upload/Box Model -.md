Box Model -


Content — The actual text, image, or other content.

Padding — Space between content and border.

Border — The boundary surrounding padding and content.

Margin — Space outside the border, separating elements.


Important Flexbox properties
Property-Purpose
display: flex-Activates Flexbox
flex-direction-Sets row or column direction
justify-content-Aligns items along the main axis
align-items-Aligns items along the cross axis
gap-Adds space between items
flex-wrap-Allows items to move to another line

Remember: With flex-direction: row, the main axis is horizontal. With column, it is vertical.

space-between: places space between items.

center: centers items along the relevant axis.

flex-start: aligns items toward the start.

flex-end: aligns items toward the end.ex


grid-template-columns: repeat(3, 1fr);

It creates three equal-width columns.
repeat(3, ...) means repeat three times.
1fr means one fraction of the available grid space.