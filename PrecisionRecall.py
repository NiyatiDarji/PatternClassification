# Plot precision-recall curve

import matplotlib.pyplot as plt

precision = [0.7894736842105263, 0.2727272727272727,  0.7894736842105263]
recall= [0.75, 0.75, 0.75]
plt.plot(recall,precision,marker = 's',color = 'r',markerfacecolor = 'b')
for i_x, i_y in zip(recall, precision):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.title('Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()