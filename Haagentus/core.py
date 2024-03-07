import numpy as np
import scipy.stats as stats

def anova_table(data:list):  
      
    # new_data = np.array(data)
    # for i in range(len(new_data)):
    #     if i == 0:
    #         new_data = np.array([new_data[i]])
    #     else:
    #         new_data = np.append(new_data, [new_data[i]], axis=0)
    
    data = np.array(data)
            
    grand_mean = np.mean(data)
    ss_total = np.sum((data - grand_mean) ** 2)
    ss_humidity = np.sum((np.mean(data, axis=1) - grand_mean) ** 2) * data.shape[1]
    ss_plastic_type = np.sum((np.mean(data, axis=0) - grand_mean) ** 2) * data.shape[0]
    
    ss_error = ss_total - ss_humidity - ss_plastic_type
    
    df_humidity = data.shape[0] - 1
    df_plastic_type = data.shape[1] - 1
    df_error = df_humidity * df_plastic_type
    df_total = np.prod(data.shape) - 1
    
    ms_humidity = ss_humidity / df_humidity
    ms_plastic_type = ss_plastic_type / df_plastic_type
    ms_error = ss_error / df_error
    f_humidity = ms_humidity / ms_error
    f_plastic_type = ms_plastic_type / ms_error
    
    p_humidity = stats.f.sf(f_humidity, df_humidity, df_error)
    p_plastic_type = stats.f.sf(f_plastic_type, df_plastic_type, df_error)

    print('요인\t\t제곱합\t\t자유도\t\t평균제곱\t\tF-통계량\t\tP-value')
    print('A\t\t{:.3f}\t\t{}\t\t{:.3f}\t\t{:.3f}\t\t{:.3f}'.format(ss_humidity, df_humidity, ms_humidity, f_humidity, p_humidity))
    print('B\t\t{:.3f}\t\t{}\t\t{:.3f}\t\t{:.3f}\t\t{:.3f}'.format(ss_plastic_type, df_plastic_type, ms_plastic_type, f_plastic_type, p_plastic_type))
    print('오차\t\t{:.3f}\t\t{}\t\t{:.3f}'.format(ss_error, df_error, ms_error))
    print('총합\t\t{:.3f}\t\t{}'.format(ss_total, df_total))
    
    
    
    
    
    