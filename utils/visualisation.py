import matplotlib.pyplot as plt

def colorgradient(RGB1, RGB2, n):
    dRGB = [float(x2-x1)/(n-1) for x1, x2 in zip(RGB1, RGB2)]
    gradient = [tuple([float(x+k*dx)/255 for x, dx in zip(RGB1, dRGB)]) for k in range(n)]
    return gradient


def summary(fav, scoring, mins, maxs, worst_es, worst_wp, labels):
    print('worst seed regarding winner probabilities', worst_wp[0], worst_wp[1])
    print('worst seed regarding expected score', worst_es[0], worst_es[1], '\n')

    for i in labels:
        print(f'player {i} win prob:', f'min = {mins[i]:.4f},',
            f'max = {maxs[i]:.4f},',
            f'favorite in {fav[i]}',
            f', topscorer in {scoring[i]}')


def visualize_bracket_analysis(results, labels, matrix, axs):
    NB = len(labels)
    win_dist = [[result['WinProb'][i] for result in results] for i in labels]
    exp_dist = [[result['ExpectedScore'][i] for result in results] for i in labels]

    axs[0].imshow(matrix)

    axs[1].violinplot(win_dist)
    axs[1].set_xticks(list(range(NB+1)), labels=[None]+[f'S{i}' for i in labels])
    axs[1].set_title('Seed Win Prob')

    axs[2].violinplot(exp_dist)
    axs[2].set_xticks(list(range(NB+1)), labels=[None]+[f'S{i}' for i in labels])
    axs[2].set_title('Seed Exp Score')

    axs[3].hist(x=[result['GTCOR_WP'] for result in results], bins='auto', rwidth=0.85)
    axs[3].set_xticks([0.4, 0.6, 0.8, 1.0])
    axs[3].set_title('Win Prob Correlation')

    axs[4].hist(x=[result['GTCOR_ES'] for result in results], bins='auto', rwidth=0.85)   
    axs[4].set_xticks([0.4, 0.6, 0.8, 1.0])
    axs[4].set_title('Expected Score Correlation')

def plot_empirical_vs_simulation(result, axs):
    axs[0].imshow(result.empirical.domain)
    axs[1].imshow(result.simulation.domain)
    
        