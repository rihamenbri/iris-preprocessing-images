data = rand(20,20);
i=0;
j=0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%standerdize the dataset%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%calculating  the mean of each colomn 
    Mean = mean(data);
%calucltin le max  :
    stan=std(data);
 %calculating the standerdized data set :
 
 for i=1:20
     for j=1:20
         z(i,j)=(data(i,j)- mean(j))/stan(j)
     end
 end
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%covarience matrix%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%matrice de covarience :
c=cov(data);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%feature
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%vector%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%valeurs :
valp=eig(c);
%Vecteurs: V and D is same as valp=eig(c)
[V,D]=eig(c);
disp(V);

%%%%%%%%%%%%%%%%%%%%%%choix %%%%%%%%%%%%%
finalei=0;
inertia=0;
taivalp=length(valp);
for i=length(valp):-1:1
    if(inertia<0.5)
        inertia = inertia +(valp(i))/sum(valp);
        finalei=i;
    end
end













